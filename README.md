# gar
Proposal: GAR - Generation-Augmented Retrieval  - go/garLLMs


Setup
 - Install Google Cloud CLI - https://cloud.google.com/sdk/docs/install-sdk
 - Enable: In your browser, navigate to the Vertex AI API Service Details page.
           Click the Enable button to enable the Vertex AI API in your Google Cloud project.
 - Install pip install --upgrade google-cloud-aiplatform
 - Choose your own project; code contains octo-gar

 How it works

 user_prompt = """what is the code for quicksort?"""


python gar-fc.py 
content:
role: "model"
parts {
  function_call {
    name: "retrieve_algorithm_from_library"
    args {
      fields {
        key: "name_algorithm"
        value {
          string_value: "quicksort"
        }
      }
    }
  }
}
