# polymorphism
# allows methods in different classes to share the same name but perform
# different tasks. You call the same method name on different objects,
# and each response in its own way.

# simply When different classes can use the same method name but implement it differently.

class Twitter:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"🐦 Tweet: '{self.content}' (280 chars max)"

class Instagram:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"📸 Instagram Post: '{self.content}' + ✨ filters"

class LinkedIn:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"

def start(social_media):
   print(social_media.post())  # Calls .post() on any object

def main():
    # Instances
    tweet = Twitter('Just learned Python polymorphism!')
    photo = Instagram('Sunset vibes 🌅')
    article = LinkedIn('Why OOP matters in 2024')

    # The polymorphic calls - same function, different outputs
    start(tweet)  # 🐦 Tweet: 'Just learned Python polymorphism!' (280 chars max)
    start(photo)  # 📸 Instagram Post: 'Sunset vibes 🌅' + ✨ filters
    start(article)  # 💼 LinkedIn Article: 'Why OOP matters in 2024' (Professional Mode)

if __name__ == "__main__":
    main()