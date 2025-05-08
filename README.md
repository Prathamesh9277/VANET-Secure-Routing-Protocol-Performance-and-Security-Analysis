# VANET Simulation with Cryptographic Validation

## Overview
This project simulates a Vehicular Ad-Hoc Network (VANET) where vehicles communicate via Route Request (RREQ) and Route Reply (RREP) messages. The messages are validated using Ed25519 digital signatures and SHA-256 hashing to ensure authenticity and integrity.

The simulation includes features like cryptographic signing, message verification, and the ability to simulate malicious tampering by a compromised vehicle (attacker). The main goal is to demonstrate how cryptographic checks help ensure secure communication in vehicular networks.

---

## Features
- **Vehicle Communication Simulation**: Vehicles in the network broadcast Route Request (RREQ) and unicast Route Reply (RREP) messages.
- **Message Authentication**: Uses Ed25519 signatures for authentication and SHA-256 hashing for integrity checks.
- **Cryptographic Validation**: Verifies the integrity and authenticity of messages as they traverse the network.
- **Tampering Scenarios**: Simulates a malicious node that tampers with messages in-flight to demonstrate the impact of compromised vehicles.
- **Metrics Reporting**: Tracks and reports the validity of each message, including hash and signature verification results.

---

## Components

### 1. **main.py**: Simulation Setup and Execution
   - The entry point of the simulation.
   - Initializes vehicles and cryptographic keys.
   - Simulates the broadcasting of Route Request (RREQ) messages from the source vehicle.
   - Verifies the integrity and authenticity of messages using cryptographic checks.
   - If the destination vehicle receives a valid RREQ, it sends a Route Reply (RREP).
   - Logs metrics for each message processed (valid/invalid).

### 2. **config.py**: Configuration File
   - Stores all the configurable parameters of the simulation.
   - You can modify settings such as the number of vehicles, attacker behavior, and specific vehicle IDs for the source and destination.

### 3. **vehicle.py**: Vehicle Class
   - Represents a vehicle in the VANET network.
   - Each vehicle has an ID and stores keys for cryptographic operations.
   - Can send and receive messages (RREQ and RREP).

### 4. **crypto_utils.py**: Cryptographic Utilities
   - Contains functions for cryptographic operations, including:
     - `init_keys(ids)`: Initializes Ed25519 private/public key pairs for each vehicle ID.
     - `add_hash(msg)`: Computes and adds an SHA-256 hash to the message.
     - `sign_message(msg, sender_id)`: Signs a message with the sender’s private key.
     - `verify_message(msg, sender_id)`: Verifies the integrity (hash) and authenticity (signature) of the message.

### 5. **network.py**: Network Communication
   - Handles the broadcasting and unicast of RREQ and RREP messages between vehicles.
   - Simulates the vehicle-to-vehicle message passing mechanism.
   - Can also simulate tampering if an attacker is enabled.

### 6. **routing.py**: Routing Logic
   - Defines the logic for creating RREQ and RREP messages.
   - Builds paths for route requests and replies.

### 7. **metrics.py**: Metrics Collection
   - Tracks and logs the results of the cryptographic message validation.
   - Reports the number of valid and invalid messages, as well as the reasons for failure (e.g., hash mismatch, signature failure).

---

## Installation and Setup

### Prerequisites
Ensure you have Python 3.x installed on your machine. You will also need to install the required Python libraries.

1. **Install Python Dependencies**
   - You can install the required dependencies using `pip`:

   ```bash
   pip install cryptography
