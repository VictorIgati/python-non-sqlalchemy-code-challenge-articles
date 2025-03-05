# Define the Article class
class Article:

    # Class variable to store all instances of Article
    all = []

    # Initialize an Article instance with author, magazine, and title
    def __init__(self, author, magazine, title):
        # Ensure the author is an instance of Author
        if not isinstance(author, Author):
            raise ValueError("Author must be an Author instance")
        # Ensure the magazine is an instance of Magazine
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        # Ensure the title is a string between 5 and 50 characters
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        # Set the instance variables to private 
        self._author = author
        self._magazine = magazine
        self._title = title
        # Add the instance to the class variable list
        Article.all.append(self)

    # Property to get the title of the article and allows read only access to the title
    @property
    def title(self):
        return self._title

    # Property to get the author of the article
    @property
    def author(self):
        return self._author

    # Setter to change the author of the article
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author

    # Property to get the magazine of the article
    @property
    def magazine(self):
        return self._magazine

    # Setter to change the magazine of the article
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine


# Define the Author class
class Author:
    # Class variable to store all instances of Author
    all = []

    # Initialize an Author instance with a name
    def __init__(self, name):
        # Ensure the name is a non-empty string
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        # Set the instance variable
        self._name = name
        # Add the instance to the class variable list
        Author.all.append(self)

    # Property to get the name of the author and it is read only access to the name of the author
    @property
    def name(self):
        return self._name

    # Method to get all articles written by the author
    def articles(self):
        #List comprehension to get all articles written by the author
        return [article for article in Article.all if article.author == self]

    # Method to get all magazines the author has written for
    def magazines(self):
        #Set comprehension to  returns a list of all unique Magazine instances where the author has written articles. By using a set, it ensures that no magazine is listed more than once.
        return list({article.magazine for article in self.articles()})

    # Method to add a new article written by the author
    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        return Article(self, magazine, title)

    # Method to get all unique topic areas the author has written about
    def topic_areas(self):
        #Set comprehension to returns a list of all unique categories (topic areas) of magazines where the author has written articles. By using a set, it ensures that no category is listed more than once. 
        return list({magazine.category for magazine in self.magazines()})


# Define the Magazine class
class Magazine:
    # Class variable to store all instances of Magazine
    all = []

    # Initialize a Magazine instance with a name and category
    def __init__(self, name, category):
        # Ensure the name is a string between 2 and 16 characters
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        # Ensure the category is a non-empty string
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")

        # Set the instance variables
        self._name = name
        self._category = category
        # Add the instance to the class variable list
        Magazine.all.append(self)

    # Property to get the name of the magazine
    @property
    def name(self):
        return self._name

    # This setter ensures that the name attribute can only be updated with a valid string that meets the length requirements.
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (2 <= len(new_name) <= 16):
            self._name = new_name

    # Property to get the category of the magazine
    @property
    def category(self):
        return self._category

    # Setter to change the category of the magazine
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category

    # Method to get all articles in the magazine
    def articles(self):
        # List comprehension to retrieve all articles published in the current magazine. It filters the global Article.all list to include only those articles whose magazine attribute matches the current magazine instance (self).
        return [article for article in Article.all if article.magazine == self]

    # Method to get all unique authors who have written for the magazine
    def contributors(self):
        # Set comprehension to return a list of all unique Author instances who have written articles for the magazine. By using a set, it ensures that no author is listed more than once. 
        return list({article.author for article in self.articles()})

    # Method to get all titles of articles in the magazine
    def article_titles(self):
        # List comprehension: The article_titles method retrieves all article titles published in the current magazine. It uses the articles method to get a list of all articles associated with the magazine and then extracts the title attribute from each article.
        return [article.title for article in self.articles()]

    # Method to get authors who have written more than 2 articles for the magazine
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            # Get the author of the article
            author = article.author
            # Count the number of articles written by each author
            author_counts[author] = author_counts.get(author, 0) + 1
        # Return authors who have written more than 2 articles
        return [author for author, count in author_counts.items() if count > 2]

    # Class method to get the magazine with the most articles
    @classmethod
    def top_publisher(cls):
        # Return None if there are no magazines
        if not cls.all:
            return None
        # keep track of the maximum number of articles found so far. Starting with -1 ensures that any valid article count (which is always non-negative) will be greater than this initial value. 
        max_articles = -1
        # This initializes a variable to store the magazine with the most articles. Initially, it is set to None because no magazine has been evaluated yet.
        top_magazine = None
        # Iterate through all magazines to find the one with the most articles
        for magazine in cls.all:
            article_count = len(magazine.articles())
            #checks whether the current magazine  has more articles than the previous maximum magazine_airticles 
            if article_count > max_articles:
                max_articles = article_count
                top_magazine = magazine
                #This ensures that after iterating through all magazines, the top_magazine variable will hold the magazine with the highest article count.
        # Return the magazine with the most articles
        return top_magazine