# Enhanced File Classifier

## Scope:

- Need to identify and categorize over 100,000 documents a day before automations can begin
- Repo has basic endpoint that for classifying files by their file names (super basic, not robust, scalable)
- Limitations

  - Handling poorly named files
  - Processing larger number of files
  - Adapting to new industries easily (hardcoding in the labels for the different categories)

- Idea: could use some unsupervised learning algo to group similar documents, a learned function to classify documents instead of hardcoded ones

## Task:

Improve classifier by adding features and optimizations to handle:

1. poorly named files
2. scaling to new industries
3. procesing larger volumes of documents

## Suggestions:

1. Enhacing the Classifier
   What are the limitations in the current classifier that's stopping it from scaling?

- Right now the possible "file types" are hard coded into the classifier, so when scaling to new industries with different types of files would need to hardcode in those new file types

  How might you extend the classifier with additional technologies, capabilities, or features?

- Using AI to group similar documents on its own then we can assign the correct corresponding file types to each group

2. Productionising the Classifier
   How can you ensure the classifier is robust and reliable in a production environment?

- Need to have better error handling, more useful logged information for debugging and handling exceptions

  How can you deploy the classifier to make it accessible to other services and users?

- Need to make it so that the code can easily be applied to other situations (a function that takes in specific information)

Possible Ideas / Suggestions

- Train a classifier to categorize files based on the text content of a file
- Generate synthetic data to train the classifier on documents from different industries
- Detect file type and handle other file formats (e.g., Word, Excel)
- Set up a CI/CD pipeline for automatic testing and deployment
- Refactor the codebase to make it more maintainable and scalable

## Work flow

1. Extract text content from different files
   - Need to handle different file types, but will start with extracting just a few to start (get the pipeline up and running)
2. Group document using K-means or something else

# Code Info

- All the packages used should be in the requirements.txt file
- Also use Tesseract OCR, so may need to install: brew install tesseract
