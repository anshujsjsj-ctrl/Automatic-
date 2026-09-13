# VIP Like API

This API allows you to send likes to player profiles in a game (presumably Free Fire), using a set of tokens for different servers. It includes functionality for loading tokens, sending likes in batches, profile checks, and encryption.

## Features

- **Token Batch Management**: Automatically manages and rotates token batches to send likes.
- **Profile Check**: Allows profile check before and after sending likes, fetching and comparing the number of likes.
- **Encryption**: Encrypts data using AES encryption for secure communication.
- **Support for Multiple Servers**: Supports multiple servers with different token files and endpoints.

## Supported Servers

- **India (IND)**
- **Bangladesh (BD)**
- **Brazil (BR)**
- **United States (US)**
- **South America (SAC)**
- **North America (NA)**

## Endpoints

### `/like` - Send Likes

This endpoint is used to send likes to a player's profile. It uses either a rotating batch of tokens or a randomly selected batch of tokens.

#### Parameters:

- `uid` (required): The UID of the player you want to send likes to.
- `server_name` (required): The server name (`IND`, `BD`, `BR`, `US`, `SAC`, `NA`).
- `random` (optional): Set to `true` to use random batch selection of tokens, otherwise `false` (default).

#### Example Request:

## GET /like?uid=123456789&server_name=IND&random=true

#### Example Response:

```json
{
  "LikesGivenByAPI": 50,
  "LikesafterCommand": 100,
  "LikesbeforeCommand": 50,
  "PlayerNickname": "Player123",
  "UID": 123456789,
  "status": 1,
  "Note": "Used visit token for profile check and random batch of 189 tokens for like sending.",
  "Owner": "@XEROX_MODS",
  "Tg": "SEXTYMODS"
}```

## HARD EADIT SUPPORT TG CHHANEL @XEROX_LIKES 

## MAIN CHHANEL @SEXTY_MODS

---

Now the `Owner` is `"XEROX_MOD"` and the Telegram handle (`Tg`) is `@XEROX_LIKES`. You can copy and paste this into your `README.md`. Let me know if you need any further changes!