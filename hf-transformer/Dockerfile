FROM huggingface/transformers-pytorch-cpu:latest

RUN pip install --no-cache-dir "transformers[serving]"

EXPOSE 8080

CMD ["transformers-cli", "serve", "--model", "Qwen/Qwen2.5-0.5B-Instruct", "--task", "text-generation", "--device", "-1", "--host", "0.0.0.0", "--port", "8080"]