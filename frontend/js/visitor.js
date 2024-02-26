
        // Define a function that takes the Azure function URL as a parameter
        function callAzureFunction(url) {
            // Send an HTTP GET request to the Azure function using fetch
            fetch(url, {method: "GET"})
            .then(data => {
                // Convert the response data to a JSON object
                return data.json();
            })
            .then(post => {
                // Display the JSON data in the div element
                document.getElementById("azure").innerText += " " + post;
            })
            .catch(err => {
                // Handle any errors that may occur
                console.log(err);
            })
        }

        // Call the function with the Azure function URL
        var url = "https://cloud-resume-api-dev.azurewebsites.net/api/HttpTrigger1?code=c1JgM10vKTzwDxPYkR1g48behuWpGbSLrKDLxcZXums6AzFuVA71_w=="
        callAzureFunction(url);
 