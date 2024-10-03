# Crossmint Coding Challenge

## Overview

This repository contains the solution for the Crossmint coding challenge, where the objective was to build a megaverse map that includes different astral objects such as **POLYAnets**, **SOLoons**, and **comETHs**.

I programmatically generated and adjusted a map based on the Crossmint logo. The map includes different astral objects with specific rules regarding their placement and behavor:

- 🌙 **SOLoons** can only be placed adjacent to 🪐 **POLYAnets** and have different colors.
- ☄ **comETHs** can be placed alone in the universe but must face a certain direction.

I created a Python script to retrieve the goal map and adjust it by adding or removing the objects as necessary.

## Key Features

### 1. **Fetching the Goal Map:**
- The script retrieves the current goal map for the challenge using the provided API.
- This goal map serves as the blueprint for where astral objects should be placed in the megaverse.

### 2. **Astral Objects:**
- **POLYAnets**: Represent the central structure and can be placed freely at specific positions.
- **SOLoons**: Must always be adjacent to a **POLYAnet** and come in various colors.
- **comETHs**: Stand-alone object that can appear anywhere, facing a particular direction (e.g., "up", "down").

### 3. **Modifying the Megaverse:**
- The script checks the goal map to determine the required object for each position.
  - **If "POLYAnet"**: A 🪐 **POLYAnet** is placed.
  - **If "Soloon"**: A 🌙 **SOLoon** with the specified color is placed adjacent to a **POLYAnet**.
  - **If "comETH"**: A ☄ **comETH** is placed facing the appropriate direction.
  - **If "SPACE"**: Any existing objects in that position are deleted.

### 4. **API Interaction:**
- **POST** requests are used to create and place the objects (**POLYAnets**, **SOLoons**, **comETHs**).
- **DELETE** requests are used to remove objects from positions that should be empty (i.e., marked as "SPACE").

## Result

Below is the final result, displaying the megaverse map, which includes **POLYAnets**, **SOLoons**, and **comETHs**, arranged to replicate the Crossmint logo:

![Crossmint logo](https://github.com/user-attachments/assets/61c41d68-4e26-4f00-b759-29e1a8222372)

