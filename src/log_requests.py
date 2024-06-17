from mitmproxy import http
import json
import urllib.parse


def request(flow: http.HTTPFlow) -> None:
    if "logging_client_events" in flow.request.pretty_url:
        try:
            # Parse the request content to get the payload
            parsed_content = urllib.parse.parse_qs(flow.request.text)
            message = parsed_content.get("message")

            if message:
                # Decode the message and parse it as JSON
                parsed_message = json.loads(message[0])

                # Log the parsed message to a JSON file
                with open("../data/logging_client_events.json", "a") as log_file:
                    json.dump(parsed_message, log_file, indent=4)
                    log_file.write(",")
                    log_file.write("\n")
        except Exception as e:
            print(f"Error processing request: {e}")
