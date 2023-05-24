# Class inheritance

`class ExampleChildClass(ExampleParentClass)`

ExampleChildClass can now use ExampleParentClass's content, and has the same attributes, plus whatever attirbutes it has by itself.

```


ExampleParentClass():

"""actually accomplishes somehting lin life"""

    __money = 0

    def __init__(self, starting_capital = 0):

        """imas"""

        if isinstance(starting_capital, int) is True:

            self.money += starting_capital

    def do_work():

        """does work"""

        print "this print function is hard work"

    def get_paid(self):

        print "made some money"

        self.cash += 999

ExampleChildClass(ExampleParentClass):

    """about to do what's called a pro gamer move"""

    def __init__(self, starting_cash, arg2)

        """comes into existance.

        essentially copypaste's the code from parent's __init__

        useful if parent's __init__ performs some starting operations, such as making connections

        """

        super.__init__(starting_cash)

    def take_credit(self):

        """uses the parent's do_work method.

        does not need it's own work.

        """

        super.do_work()

    def do_work(self):

        """does own work"""

        print "just did my own work"

    def get_paid(self):

        """what happens when child tries to get paid

        overrides what the parent would have done when getting paid

        """

        self.money += 20

        print "*cries*"

```
