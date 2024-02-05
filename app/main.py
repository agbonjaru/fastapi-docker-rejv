from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
import time

app = FastAPI()

# Function to calculate Pi using Leibniz's formula
def calculate_pi():
    num_iteration = 1000000  # This can be adjusted for accuracy.
    pi_approx = 0.0

    for k in range(num_iteration):
        pi_approx += ((-1) ** k) / (2 * k + 1)

    return 4 * pi_approx

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Calculate Pi using Leibniz's formula
    pi_value = calculate_pi()

    # Generate Python random pseudo-random sequence
    random_sequence = [random.random() for _ in range(5)]

    # Get POSIX timestamp
    posix_timestamp = time.time()

    # HTML response
    html_content = """
    <html>
        <head>
            <title>FastAPI Web Page</title>
        </head>
        <body>
            <h1>Web Page Output</h1>
            <p>Number Pi (Leibniz's formula): {pi_value}</p>
            <p>Python Random Pseudo-Random Sequence: {random_sequence}</p>
            <p>POSIX Timestamp: {posix_timestamp}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content.format(pi_value=pi_value, random_sequence=random_sequence, posix_timestamp=posix_timestamp))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
