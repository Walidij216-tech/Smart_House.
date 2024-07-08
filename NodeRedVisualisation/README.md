# Node-RED Visualization

This Node-RED flow provides a simple temperature monitoring dashboard using randomly generated data.

## Flow Explanation

- **Inject Node**: Sends a date payload every 10 seconds.
- **Function Node**: Generates a random temperature value between 20°C and 30°C.
- **Debug Node**: Outputs the temperature value to the debug console.
- **UI Chart Node**: Displays the temperature data in a line chart.

## Installation and Usage

1. Install Node-RED on your Raspberry Pi.
2. Import the `flow.json` into your Node-RED workspace.
3. Deploy the flow.
4. Access the dashboard to view real-time temperature data.

For more details on Node-RED, visit [Node-RED Official Documentation](https://nodered.org/docs/).

