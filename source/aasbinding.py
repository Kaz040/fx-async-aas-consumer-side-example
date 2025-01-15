import requests
import base64
from jsonschema import validate
import logging

submodel_repo = "http://aasx-server:5001/submodels"


def aas_repo(payload):
    pass


def update_submodel_repo(payload):
    """
    Update means that the AAS is already existing at the data consumer side(machine builder)
    Update can be the whole submdel or a submodel element in a submodel.
    The payload element provide the hint for this.
    """
    # build URL
    submodelId_byte = payload["source"].encode("utf-8")
    submodelId_base64 = base64.b64encode(submodelId_byte).decode("utf-8")
    if len(payload["data"]["element"]["keys"]) < 2:
        url = f"{submodel_repo}/{submodelId_base64}/"
    else:
        submodel_element_path = ""
        keys = payload["data"]["element"]["keys"]
        for i in range(len(keys)):
            if keys[i]["type"] == "SubmodelElement" and i < len(keys) - 1:
                submodel_element_path = submodel_element_path + keys[i]["value"] + "."
            elif keys[i]["type"] == "SubmodelElement":
                submodel_element_path = submodel_element_path + keys[i]["value"]
        url = f"{submodel_repo}/{submodelId_base64}/submodel-elements/{submodel_element_path}"

    logging.info(f"URL = {url}")

    # send a patch request to the server to update the submodel or submodel element.

    response = requests.patch(url=url, json=payload["data"]["value"])
    if response.status_code == 204:
        logging.info("Event Forwarding Was Successful")
    else:
        logging.info(
            f"Something Bad Happens, Event Forwarding Was Not Successful\nHTTP Error Code: {response.status_code}"
        )


def model_validation(payload, schema):
    pass
