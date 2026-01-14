# Root-level client for the test connector
public isolated client class Client {

    private final string serviceUrl;
    private final string? apiKey;

    # Initialize the root-level client
    #
    # + config - Connection configuration
    # + return - Error on failure
    public isolated function init(ConnectionConfig config = {}) returns error? {
        self.serviceUrl = config.serviceUrl ?: "http://example.com";
        self.apiKey = config.apiKey;
    }

    # Sample operation in root client
    #
    # + message - Message to send
    # + return - Response or error
    public isolated function sendMessage(string message) returns string|error {
        return "Root client: " + message;
    }
}

# Connection configuration for the root client
public type ConnectionConfig record {|
    # Service URL
    string serviceUrl?;
    # API key for authentication
    string apiKey?;
|};
