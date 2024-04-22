import vertexai
from google.cloud import aiplatform
import vertexai.preview
from vertexai.generative_models import GenerativeModel
from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerativeModel,
    Part,
    Tool,
)

retrieve_algorithm_from_library = FunctionDeclaration(
    name="retrieve_algorithm_from_library",
    description="used to retrieve the algorithms from code library",
    parameters={
    "type": "object",
    "properties": {
        "name_algorithm": {
            "type": "string",
            "description": "the name of the algorithm to retrieve from our library"
        },
    },
         "required": [
            "name_algorithm",
      ]
  },
)

def init(): 
  vertexai.init(project='octo-gar')
  
def call_model():
  model = GenerativeModel("gemini-1.0-pro")

  retrieve_tool = Tool(
    function_declarations=[retrieve_algorithm_from_library],
  )

  user_prompt = """what is the code for quicksort?"""
  prompt = """
    
    Using the retrieve_algorithm_from_library function to search and retrieve algorithms from a library

    Answer the following question:
    """ + user_prompt 

  response = model.generate_content(
    prompt,
    tools=[retrieve_tool],
  )

  print('content:')
  print (response.candidates[0].content)


#  url = f"https://api.frankfurter.app/{params['date']}"
#  api_response = requests.get(url, params=params)
#  print (api_response.text)


init()
call_model()
