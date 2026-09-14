# Real-Time Chat App (Python Sockets)

A simple two-user command-line chat application using Python sockets and threading.

## Files

- `server.py` — listens for connections and relays messages between two clients.
- `client.py` — connects to the server and lets you send/receive messages.

## How it works

1. Run the server first. It waits for two clients to connect.
2. Run the client script twice (in two separate terminals) to simulate two users.
3. Each client enters a name, then messages typed by one client appear on the other's screen with a timestamp, like:
   ```
   [14:35] Alice: Hello
   ```
4. If one client disconnects, the other is notified.

## Run it

Start the server:
```bash
python server.py
```

Then open two more terminals and run the client in each:
```bash
python client.py
```

## Tech used

Python 3, `socket`, `threading` — no external libraries.
