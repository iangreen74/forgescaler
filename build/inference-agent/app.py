from fastapi import FastAPI, File, UploadFile, HTTPException
import onnx
import onnxruntime as ort
import numpy as np
from PIL import Image
import io

app = FastAPI()

# Use SqueezeNet (confirmed working model)
model_path = "squeezenet1.1-7.onnx"

try:
    onnx_model = onnx.load(model_path)
    onnx.checker.check_model(onnx_model)
except Exception as e:
    raise RuntimeError(f"ONNX model validation failed: {e}")

try:
    session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
except Exception as e:
    raise RuntimeError(f"Failed to create ONNX inference session: {e}")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read())).resize((224, 224))
        image_data = np.asarray(image).astype(np.float32) / 255.0

        if image_data.ndim == 2:
            image_data = np.stack((image_data,) * 3, axis=-1)

        image_data = np.transpose(image_data, (2, 0, 1))[np.newaxis, ...]
        input_name = session.get_inputs()[0].name
        output = session.run(None, {input_name: image_data})[0]

        return {"prediction": output.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {e}")
