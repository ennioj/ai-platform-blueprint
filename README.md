# AI Platform Examples

This repository demonstrates reference implementations for deploying AI workloads in a **cloud-native, production-oriented way**, focusing on Kubernetes orchestration, GPU scheduling, and API integration.

The repository currently contains some examples:

1. **vLLM on GPU**  
   Demonstrates deploying a large language model using [vLLM](https://github.com/vllm-project/vllm) on a Kubernetes cluster with GPU resources. This example shows how to configure pods with GPU scheduling, resource requests/limits, and exposes an HTTP API for inference.

2. **RAG API (Retrieval-Augmented Generation)**  
   Provides a reference implementation for a RAG-style pipeline using a vector store and a transformer model. Includes a FastAPI server that handles retrieval and generation, illustrating how to deploy such a system on Kubernetes.

3. **Kubernetes Deployment Example (HuggingFace Transformer on GPU)**
   This is a simple deployment of a HuggingFace transformer model (e.g., `distilbert-base-uncased`) using a GPU-enabled pod.
   

## Goals of the Repository

- Provide **production-ready deployment examples** for AI workloads.
- Demonstrate **Kubernetes best practices**: resource requests, GPU scheduling, environment variables, and service exposure.
- Show **API integration patterns** for LLM inference and retrieval pipelines.
- Provide clear, **reusable templates** for future AI deployment projects.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/ennioj/ai-platform-examples.git
   cd ai-platform-examples
