#include <WiFi.h>
#include <WebServer.h>

// WiFi credentials
const char* ssid = "your-wifi-id";
const char* password = "wifi-passw";

// Define the pin for the gas sensor
const int gasSensorPin = 34;

// Create a web server on port 80
WebServer server(80);

void setup() {
  Serial.begin(115200);  // Initialize serial communication at 115200 baud rate
  pinMode(gasSensorPin, INPUT);  // Set the gas sensor pin as an input

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Define the root endpoint
  server.on("/", handleRoot);
  server.begin();
}

void loop() {
  server.handleClient();  // Handle incoming client requests
  int gasLevel = analogRead(gasSensorPin); 
  Serial.print("Gas Level: "); // Print gas level to serial monitor
  Serial.println(gasLevel);
  server.send(200, "text/plain", String(gasLevel));  // Send as numeric value
  delay(2000); // Wait for 2 seconds
}

void handleRoot() {
  int gasLevel = analogRead(gasSensorPin);  // Read gas sensor value
  server.send(200, "text/plain", String(gasLevel));  // Send gas sensor value as response
}
