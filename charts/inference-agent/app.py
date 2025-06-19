from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import onnxruntime as ort
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Load ONNX model
model_path = "squeezenet1.1-7.onnx"
session = ort.InferenceSession(model_path)

# SqueezeNet expects input shape: [1, 3, 224, 224]
def preprocess_image(image: Image.Image) -> np.ndarray:
    image = image.resize((224, 224))
    image = np.array(image).astype(np.float32)
    if image.ndim == 2:  # grayscale
        image = np.stack([image]*3, axis=-1)
    elif image.shape[2] == 4:  # remove alpha channel
        image = image[:, :, :3]
    image = image / 255.0
    image = image.transpose(2, 0, 1)  # HWC to CHW
    image = np.expand_dims(image, axis=0)
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        input_tensor = preprocess_image(image)

        input_name = session.get_inputs()[0].name
        outputs = session.run(None, {input_name: input_tensor})

        output_tensor = outputs[0]
        predicted_class = int(np.argmax(output_tensor))

        return JSONResponse(content={
            "predicted_class_index": predicted_class,
            "confidence": float(np.max(output_tensor))
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
