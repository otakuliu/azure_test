from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Azure Web App Python Demo</h1>
    <p>Deploy success.</p>
    <ul>
      <li><a href="/health">/health</a></li>
      <li><a href="/error">/error</a> (test 500 logs)</li>
      <li><a href="/echo?name=azure">/echo?name=azure</a></li>
    </ul>
    """

@app.route("/health")
def health():
    app.logger.info("health endpoint hit")
    return jsonify(status="ok")

@app.route("/echo")
def echo():
    name = request.args.get("name", "world")
    app.logger.info("echo endpoint hit with name=%s", name)
    return jsonify(message=f"hello, {name}")

@app.route("/error")
def error():
    app.logger.error("intentional test error endpoint triggered")
    raise RuntimeError("intentional test error for logging")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
