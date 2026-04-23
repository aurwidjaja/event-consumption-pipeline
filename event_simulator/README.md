# 📦 Event-Driven Data Pipeline Simulator

## 🧠 Overview

This project simulates a real-world event-driven (small) backend system where multiple services emit inconsistent events that must be ingested, normalized, processed, and stored reliably.

The goal is to model the challenges of production data pipelines:

* inconsistent schemas
* messy data formats
* partial failures
* duplicate events
* asynchronous processing

This system mimics patterns used in modern backend architectures (e.g. event streaming systems in fintech and marketplaces like Stripe-style payment pipelines).

---

## 🎯 Goals

By building this system, I aim to demonstrate:

* Design of event-driven architectures
* Handling of schema inconsistency and drift
* Data normalization and transformation pipelines
* Failure handling (retries + dead-letter queue)
* Asynchronous processing concepts
* Basic observability (logging + metrics)

---

## 🏗️ System Architecture

```
Event Producers → Event Bus (Queue) → Processing Layer → Storage Layer
                          ↓
                   Dead Letter Queue
```

---

## 🔌 Components

### 1. Event Producers

Simulated services that generate raw events.

Examples:

* order service
* payment service
* authentication service

Each producer emits:

* inconsistent field names
* varying data types
* missing or extra fields
* corrupted values (simulated)

---

### 2. Event Bus (Queue Layer)

Acts as the central buffer between producers and consumers.

Responsibilities:

* temporarily stores incoming events
* decouples producers from consumers
* supports asynchronous processing

Implementation:

* `asyncio.Queue` or `queue.Queue`

---

### 3. Processing / Normalization Layer

Transforms raw events into a unified schema.

Responsibilities:

* schema mapping (field renaming)
* type normalization (string → float/int/datetime)
* handling missing or invalid fields
* resolving inconsistent formats

Output:
Canonical event format:

```json id="canon_spec"
{
  "event_type": "order | payment | auth",
  "user_id": int,
  "amount": float,
  "timestamp": datetime,
  "source": string
}
```

---

### 4. Storage Layer

Stores processed events.

Can be implemented using:

* in-memory lists (initial version)
* JSON files
* SQLite / PostgreSQL (advanced version)

Stores:

* normalized events
* raw events (optional)
* metadata

---

### 5. Dead Letter Queue (DLQ)

Stores events that fail processing.

Used for:

* malformed data
* schema mismatches
* unresolvable errors

Structure:

```json id="dlq_spec"
{
  "event": {...},
  "error": "reason for failure",
  "timestamp": "..."
}
```

---

## ⚙️ Event Inconsistencies Simulated

The system intentionally introduces real-world data issues:

### Schema inconsistency

* `user_id`, `uid`, `user`

### Type inconsistency

* `"12"`, `12`, `"12.0"`

### Missing fields

* partially populated events

### Corrupted values

* negative amounts
* invalid timestamps
* malformed strings

### Duplicate events

* replayed or repeated messages

### Out-of-order events

* events not guaranteed to arrive in sequence

---

## 🔄 Processing Flow

1. Producer generates event
2. Event is pushed to queue
3. Consumer retrieves event
4. Event is normalized
5. Valid events → storage
6. Invalid events → DLQ
7. Metrics/logs updated

---

## 🧪 Simulation Requirements

The system must support:

* multiple concurrent producers
* multiple concurrent consumers
* configurable event volume
* random delays to simulate real systems
* configurable error rate

---

## 📊 Observability (Minimum Requirements)

Track:

* total events processed
* success rate
* failure rate
* DLQ size
* processing latency (optional)

Logging should include:

* event source
* processing outcome
* error reasons

---

## 🚀 Stretch Goals (Optional)

If time permits:

### 1. Async processing

Use `asyncio` to simulate real-time pipelines

### 2. Retry system

Retry failed events with backoff

### 3. Schema registry

Maintain versioned schemas per service

### 4. Event replay

Reprocess historical raw events

### 5. Idempotency handling

Prevent duplicate processing

### 6. Basic API layer

Expose:

* `/events`
* `/metrics`
* `/dlq`

---

## 🧱 Suggested Tech Stack

* Python 3.10+
* asyncio or threading
* dataclasses or pydantic (optional)
* SQLite / JSON storage
* logging module

---

## 🧭 Success Criteria

This project is successful if:

* It can process multiple event streams concurrently
* It correctly normalizes inconsistent data
* It gracefully handles failures without crashing
* It separates raw vs processed data
* It simulates real-world unpredictability

---

## 💡 Key Engineering Insight

The core challenge this project models is:

> “How do you build reliable systems on top of unreliable data?”

This is a foundational problem in backend, data engineering, and distributed systems.
