# LLM Inference Platform on Kubernetes (GPU-enabled)

## Overview

This repository outlines a reference approach for deploying and operating Large Language Model (LLM) inference workloads on Kubernetes using GPU resources.

The focus is on infrastructure and platform design considerations rather than application logic, with particular attention to scheduling constraints, cost optimization, and production trade-offs when running AI workloads at scale.

---

## Problem

Running LLM inference in production introduces constraints that differ significantly from traditional stateless services:

- GPU resources are limited and expensive
- Model loading times are high (cold start latency)
- Throughput depends on batching and memory utilization
- Horizontal scaling is non-trivial due to resource fragmentation

A naive deployment approach leads to:
- underutilized GPUs
- high operational cost
- poor latency under load

---

## Solution

This design deploys an LLM inference service on Kubernetes using GPU-enabled nodes and an optimized inference runtime (e.g. vLLM).

Key aspects:
- GPU-aware scheduling
- optimized model serving
- controlled scaling strategy
- separation of compute and orchestration concerns

---

## Architecture

### Components

- **Inference Service (vLLM-based container)**
  - Serves model inference via HTTP API
  - Supports batching for improved GPU utilization

- **Kubernetes (EKS / GKE / self-managed)**
  - Schedules workloads on GPU nodes
  - Manages lifecycle and scaling

- **GPU Node Pool**
  - Dedicated nodes with NVIDIA GPUs
  - Isolated from general workloads

---

### Data Flow

1. Client sends inference request
2. Request reaches LLM service
3. Requests may be batched internally
4. Model executes on GPU
5. Response returned to client

---

## Kubernetes Deployment

The deployment explicitly requests GPU resources:

- `nvidia.com/gpu` resource limits enforce scheduling on GPU nodes
- Replica count is kept low due to high per-instance cost
- Service exposes the inference endpoint internally

### Key Considerations

- GPU nodes must be provisioned separately (node group / node pool)
- NVIDIA device plugin must be installed on the cluster
- Node autoscaling should account for GPU provisioning delays

---

## Design Decisions

### Why vLLM (or similar runtime)

- Efficient request batching
- Better GPU memory utilization
- Improved throughput compared to naive serving

---

### Why Kubernetes

- Standard orchestration layer
- Integration with autoscaling and observability tooling
- Consistent deployment model across environments

---

### Why dedicated GPU node pools

- Prevents resource contention
- Enables targeted autoscaling strategies
- Simplifies cost attribution

---

## Trade-offs

### Cost vs Availability
- GPU nodes are expensive → keeping replicas low reduces cost
- However, fewer replicas reduce fault tolerance

---

### Latency vs Throughput
- Batching improves throughput
- But may introduce additional latency for individual requests

---

### Cold Start vs Resource Efficiency
- Keeping models loaded reduces latency
- But increases idle GPU cost

---

## Production Considerations

### Autoscaling

Traditional HPA is insufficient for GPU workloads.

Alternatives:
- queue-based scaling (e.g. Kafka, SQS)
- custom metrics (GPU utilization, request queue length)

---

### Observability

Key metrics:
- GPU utilization
- request latency
- batch size
- memory usage

Tools:
- Prometheus + Grafana
- NVIDIA DCGM exporter

---

### Cost Optimization

- Use spot instances for non-critical workloads
- Right-size GPU types based on model requirements
- Scale to zero for dev/test environments

---

### Reliability

- Model loading failures must be handled explicitly
- Readiness probes should account for model warm-up
- Rolling updates can be slow due to large model initialization

---

## Future Improvements

- Async inference via queue (Kafka-based ingestion)
- Multi-model routing layer
- Request prioritization
- Multi-tenant isolation
- Integration with API gateway and rate limiting

---

## Notes

This repository is intended as a platform design reference and not a fully production-ready system. It reflects how AI inference workloads can be integrated into a Kubernetes-based platform with attention to real-world constraints and trade-offs.