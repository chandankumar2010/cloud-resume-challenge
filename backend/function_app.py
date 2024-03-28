import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
@app.route(route="http_trigger")
#input bindings to read the document
@app.cosmos_db_input(arg_name="inputDocuments", database_name="visitor", container_name="count", connection="cosmosDBConnectionSetting")
#output bindings to write the CosmosDB Document
@app.cosmos_db_output(arg_name="outputDocuments", 
                      database_name="visitor",
                      container_name="count",
                      create_if_not_exists=False,
                      connection="cosmosDBConnectionSetting")
def http_trigger(req: func.HttpRequest, inputDocuments: func.DocumentList, outputDocuments: func.Out[func.Document]) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    views = 0  # Initialize views count

    if inputDocuments:
        try:
            doc = inputDocuments[0]  # Read existing count
            views =  doc["views"]

            views += 1  # Increment count
            
            print(type(views))
            
            #Write updated count
            doc["views"] = views
            outputDocuments.set(doc)
            
             
        except (KeyError, IndexError):
            logging.warning("Error accessing 'views' field or empty document list")
            return func.HttpResponse(
                "Error retrieving views count. Please check Cosmos DB data.",
                status_code=500,
            )

    return func.HttpResponse(
        body=f'{{"views": {views}}}',
        status_code=200,
        mimetype="application/json",
    )
    

