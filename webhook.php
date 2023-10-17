<?php

$apiKey = 'patmMGuVwBcLRQjFP.bf7cb18171d9f849b5e49b7cc9c78bac4acc2f70f1b08e1ea02df56fb15bfe14';

 // Replace with your table name

// Get the raw data from the webhook (assuming it's already JSON)
$rawData = file_get_contents("php://input");

// save the raw data to webhook.txt
file_put_contents('webhook.txt', $rawData);

// Decode the JSON data
$requestData = json_decode($rawData, true);
$_SESSION['requestData'] = $requestData;
// Check if the JSON decoding was successful
if ($requestData) {
    // Extract the relevant data from $requestData
    $timestamp = $requestData['timestamp'];
    $event_name = $requestData['event_name'];
    $sender_id = $requestData['sender']['id'];
    $recipient_id = $requestData['recipient']['id'];
    $text = $requestData['message']['text'];


    if (isset($requestData['message']['attachments']) && is_array($requestData['message']['attachments'])) {
        // Extract attachment data
        $attachments = $requestData['message']['attachments'];
        $url = $attachments[0]['payload']['url'];
    } else {
        $url = null;
    }
    

    // Prepare the data to save to Airtable
    $data = [
        'records' => [
            [
                'fields' => [
                    'timestamp' => $timestamp,
                    'event_name' => $event_name,
                    'sender' => $sender_id,
                    'recipient' => $recipient_id,
                    'message_text' => $text,
                    'url' => $url,
                ],
            ],
        ],
    ];
} else {
    // JSON decoding failed
    $data = null;
}
// save to Airtable


$jsonData = json_encode($data);

$ch = curl_init();

// Define the URL
$url = "https://api.airtable.com/v0/apphJEUqvQh3Schzh/webhook";

// Set cURL options
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Authorization: Bearer patHiuc7warV2gFPY.6c839fdc393f5294a0374d6f0a7e5ad9625f50ff17aeb8ba426536ef76ca0a75",
    "Content-Type: application/json",
]);

// Execute cURL session and capture the response
$response = curl_exec($ch);

echo json_encode($response);

// Check for cURL errors
if (curl_errno($ch)) {
    echo 'Error: ' . curl_error($ch);
} else {
    // Process the response (e.g., check for success)
    $responseData = json_decode($response, true);

    // Close cURL session
    curl_close($ch);

    // Handle the response
    if ($responseData) {
        // Records were successfully created
        echo 'Records created successfully!';
        // You can also access the created records in $responseData
    } else {
        echo 'Error decoding JSON response.';
    }
}
?>