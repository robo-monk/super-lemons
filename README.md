# Super Lemons 🍋

A lightweight code execution service that supports both synchronous and asynchronous Python code evaluation powered by Cloudflare Workers.

## Features

- Dynamic code execution
- Support for asynchronous operations
- Clean separation of user-defined code and execution context
- Safe execution environment with isolated scope
- Simple HTTP interface

## How It Works

Super Lemons provides an HTTP endpoint that accepts Python code in two parts:
1. User-defined code (functions, classes, etc.)
2. Caller code (the actual execution statement)

The service executes the code and returns the result, handling both synchronous and asynchronous operations automatically.

## Usage Example

Send a POST request with your code in the following format:

```python
def greet(name):
    return f"Hello, {name}!"
---
greet("World")
```

For async functions:

```python
async def fetch_data():
    # Your async code here
    return "data"
---
await fetch_data()
```

## Security Considerations
- Code is executed in an isolated scope
- User-defined code and execution context are separated


