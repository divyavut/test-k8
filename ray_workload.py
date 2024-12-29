import ray

# Initialize Ray
ray.init(address="auto")  # Connects to the Ray head node

@ray.remote
def say_hello():
    return "Hello from Ray!"

# Submit a task to the cluster
result = ray.get(say_hello.remote())
print(result)
