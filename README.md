# Appium Automation Scripts

This repository contains a collection of Appium automation scripts written in Python. These scripts are designed to automate various tasks such as app installation, reset, state management, and UI interactions on Android devices.

## Scripts Overview

### 1. `app_install.py`
**Purpose**: Sets up an Appium server, initializes a WebDriver for an Android emulator, installs a specific app, and interacts with it.

- **Key Actions**:
  - Starts the Appium server and initializes the driver with capabilities for an Android device.
  - Installs the "General-Store" app on the emulator.
  - Activates the app and waits for a specific activity to load.
  - Terminates the app after interacting with it.

- **Usage**: Automates the process of installing an APK and verifying the app's initial state after installation.

### 2. `app_reset.py`
**Purpose**: Focuses on resetting an app to its default state, similar to `app_install.py`, but without reinstalling it.

- **Key Actions**:
  - Starts the Appium server and initializes the driver.
  - Resets the app to its original state without deleting it.
  - Interacts with specific elements within the app to verify post-reset behavior.

- **Usage**: Useful for testing scenarios where the app needs to be reset to its original state.

### 3. `app_states.py`
**Purpose**: Checks and manages the state of an app on an Android device.

- **Key Actions**:
  - Starts the Appium server and initializes the driver.
  - Retrieves the current state of a specified app (e.g., running, not running, or suspended).
  - Performs actions such as activating or terminating the app based on its state.

- **Usage**: Ideal for testing app lifecycle management and ensuring the app behaves correctly in different states.

### 4. `appium_capabilities.py`
**Purpose**: Defines and manages the desired capabilities for an Appium session, allowing customization of the WebDriver's configuration.

- **Key Actions**:
  - Defines a set of desired capabilities, including platform version, device name, and app details.
  - Initializes the Appium WebDriver with these capabilities.
  - Demonstrates how to configure and launch a test session with specific settings.

- **Usage**: Useful for setting up and customizing test environments for different devices and app configurations.

### 5. `device_event.py`
**Purpose**: Handles device-level events such as orientation changes or key presses during a test session.

- **Key Actions**:
  - Starts the Appium server and initializes the driver.
  - Performs device events like changing screen orientation or pressing hardware keys.
  - Verifies the app's response to these device events.

- **Usage**: Ensures that the app responds correctly to various device events, which is critical for apps that rely on hardware interactions.

### 6. `long_click.py`
**Purpose**: Automates the process of performing a long click gesture on a specific element within an Android app.

- **Key Actions**:
  - Navigates through the app to locate a specific UI element.
  - Performs a long click gesture on the identified element.
  - Verifies that the expected menu or option appears after the long click.

- **Usage**: Tests the app's handling of long-click gestures, commonly used for context menus or additional options.

## How to Use
1. Clone this repository.
2. Ensure you have the necessary dependencies installed (e.g., Appium, Python libraries).
3. Customize the desired capabilities or file paths as needed.
4. Run the scripts using a Python interpreter.

## Dependencies
- Python 3.x
- Appium-Python-Client
- Android SDK (for emulator setup)

## License
This project is licensed under the MIT License.