from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Sample input string
text = "The ML-DL-Learning repository is designed to provide a strong foundational understanding of essential topics in Machine Learning (ML) and Deep Learning (DL). It is structured into well-organized modules that focus on key concepts and practical implementations, making it an excellent resource for beginners and those looking to reinforce their knowledge. One of the core modules covered in this repository is Preprocessing and Feature Engineering, which is critical for preparing data to improve model performance. This module includes several important subtopics. Encoding and Binning techniques help handle categorical data and discretize numerical data, respectively, enabling models to better interpret input features. Scaling and Transformation methods, such as standard scaling (Z-score normalization) and log transformations, are used to normalize data distributions and reduce bias, which can significantly enhance the accuracy and convergence of ML algorithms. Additionally, the Text Processing section offers tools and methods for preprocessing textual data, a vital step in natural language processing (NLP) tasks. The repository is continuously evolving, with plans to add more modules, including a dedicated Regex Python module for learning and practicing regular expressions.To get started, users can clone the repository and explore the Python scripts within each topic folder to understand the implementations. Contributions are welcome, encouraging the community to expand and improve the content. Overall, ML-DL-Learning serves as a comprehensive guide to mastering foundational ML and DL preprocessing techniques, empowering learners to build robust models."

# Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()

# Tokenize the input text into words
words = word_tokenize(text)

# Lemmatize each word
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]  # Assuming verb for "running"

# Join the lemmatized words back into a string
lemmatized_text = " ".join(lemmatized_words)

print("Original Text:", text)
print("Lemmatized Text:", lemmatized_text)
