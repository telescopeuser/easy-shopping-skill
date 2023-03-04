from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder

class EasyShopping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

#    @intent_file_handler('shopping.easy.intent')
#    def handle_shopping_easy(self, message):
#        self.speak_dialog('shopping.easy')


# Use case 1
    
    @intent_handler('view.goods.intent')
    def handle_view_goods(self, message):
#        self.speak('Taking a photo now. Please wait a second for me to get the result.')
#        self.speak('I find some goods here, you can ask me whatever goods you want.')
        category_label = message.data.get('item')
#        str = 'yes, I find ' +  category_label + ' in front of you'
#        self.speak(str)
        self.speak_dialog('take.photo', {'item': str(category_label)})

    @intent_handler('is.there.any.goods.intent')
    def handle_is_there_any_goods(self, message):
        category_label = message.data.get('category')
        str = 'yes, I find ' +  category_label + ' in front of you'
        self.speak(str)


# Use case 2

    @intent_handler(IntentBuilder('AskItemBrand').require('Brand').build())
    def handle_ask_item_brand(self, message):
        self.speak('I am talking about the brand of the item')


def create_skill():
    return EasyShopping()

