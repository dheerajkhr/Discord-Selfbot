import discord
from discord.ext import commands

class NotForth:
    def __init__(self, bot):
        self.bot = bot
        self.version = "0.1.0"

    ###########
    # Functions
    ###########
    
    ## Stack manipulation
    
    def func_dup(self, top):
        return [top, top]
    
    def func_drop(self, top):
        return []
    
    def func_swap(self, top, next):
        return [top, next]
    
    def func_nip(self, top, next):
        return [top]
    
    def func_over(self, top, next):
        return [top, next, top]
    
    def func_tuck(self, top, next):
        return [next, top, next]
    
    def func_rot(self, top, next, third):
        return [top, third, next]
    
    def func_rotr(self, top, next, third):
        return [next, top, third]
    
    ## Numerical
    
    def func_plus(self, y, x):
        return [x+y]
    
    def func_minus(self, y, x):
        return [x-y]
    
    def func_star(self, y, x):
        return [x*y]
    
    def func_div(self, y, x):
        return [x//y]
    
    ## Boolean
    
    def func_true(self):
        return [True]
    
    def func_false(self):
        return False
    
    def func_bool(self, top):
        return [bool(top)]
    
    def func_not(self, top):
        return [not top]
    
    def func_and(self, b, a):
        return [a and b]
    
    def func_or(self, b, a):
        return [a or b]
    
    def func_eq(self, b, a):
        return [a == b]
    
    def func_neq(self, b, a):
        return [a != b]
    
    def func_lt(self, b, a):
        return [a < b]
    
    def func_gt(self, b, a):
        return [a > b]
    
    def func_leq(self, b, a):
        return [a <= b]
    
    def func_geq(self, b, a):
        return [a > b]
    
    ## Sets
    
    def func_emptyset(self):
        return [set()]
    
    def func_newset(self, top):
        return [{top}]
    
    def func_cons(self, top, next):
        next.add(top)
        return [next]
    
    def func_unpack(self, collection):
        return collection
    
    def func_len(self, collection):
        return [len(collection)]
    
    def func_union(self, y, x):
        return [x.union(y)]
    
    def func_intersection(self, y, x):
        return [x.intersection(y)]
    
    def func_intersection(self, y, x):
        return [x.intersection(y)]
    
    def func_difference(self, y, x):
        return [x.difference(y)]
    
    def func_subset(self, y, x):
        return [x.issubset(y)]
    
    def func_superset(self, y, x):
        return [x.issuperset(y)]
    
    def func_disjoint(self, y, x):
        return [x.isdisjoint(y)]
        
    ## Higher-order
    
    def func_map(self, func, collection):
        if not hasattr(self, "func_" + func):
            raise Exception("Map: unknown function '{func}'".format(func=func))
        f = getattr(self, "func_" + func)
        if f.__code__.co_argcount != 2:
            raise Exception("Map: Function '{func}' must take exactly one parameter".format(func=func))
        result = set()
        for x in collection:
            specific_result = f(x)
            if len(specific_result) != 1:
                raise Exception("Map: Result of {func} on {x} returned multiple values".format(func=func, x=x))
            result.add(specific_result[0])
        return [result]
    
    def func_filter(self, func, collection):
        # DRY...
        if not hasattr(self, "func_" + func):
            raise Exception("Map: unknown function '{func}'".format(func=func))
        f = getattr(self, "func_" + func)
        if f.__code__.co_argcount != 2:
            raise Exception("Map: Function '{func}' must take exactly one parameter".format(func=func))
        result = set()
        for x in collection:
            specific_result = f(x)
            if len(specific_result) != 1:
                raise Exception("Map: Result of {func} on {x} returned multiple values".format(func=func, x=x))
            if specific_result[0]:
                result.add(x)
        return [result]
    
    def func_antifilter(self, func, collection):
        # DRY
        # R
        # Y
        # But this is inevitable without some sort of proper lambdas or currying or something
        if not hasattr(self, "func_" + func):
            raise Exception("Map: unknown function '{func}'".format(func=func))
        f = getattr(self, "func_" + func)
        if f.__code__.co_argcount != 2:
            raise Exception("Map: Function '{func}' must take exactly one parameter".format(func=func))
        result = set()
        for x in collection:
            specific_result = f(x)
            if len(specific_result) != 1:
                raise Exception("Map: Result of {func} on {x} returned multiple values".format(func=func, x=x))
            if not specific_result[0]:
                result.add(x)
        return [result]
    
    ## Discord
    
    # If only I'd thought to pass context, so I could have func_server, when I started writing
    def func_me(self):
        return [self.bot.user]
    
    def func_user(self, id):
        user = discord.utils.find(lambda m: m.id == int(id), self.bot.get_all_members())
        if not user:
            raise Exception("Could not find user '{id}'".format(id=id))
        return [user]
    
    def func_server(self, id):
        server = self.bot.get_guild(int(id))
        if not server:
            raise Exception("Could not find server '{id}'".format(id=id))
        return [set(server.members)]
    
    def func_bot(self, member):
        return [member.bot]
    
    ## Meta
    
    def func_about(self):
        return ["""
A weird Forth-like RPN set-manipulation language, with some support for Discord members in those sets.
Mostly exists because I was bored and wanted to write a DSL. Use the Python debugger for serious work.
Due to (1) no procedural-like constructs (2) no proper higher-order functional capabilities, it is a bit useless, though technically Turing complete (tarpit)
Created by adjnouobsref (Adj)
"""]
    
    def func_help(self):
        return ["This will link to a help page eventually"]
    
    def func_ver(self):
        return [self.version]
    
    #######
    # Logic
    #######
    
    # For some reason __str__ for collections actually uses __repr__
    def custom_print(self, item):
        if type(item) == list:
            return "[" + ", ".join(map(self.custom_print, item)) + "]"
        if type(item) == set:
            return "{" + ", ".join(map(self.custom_print, item)) + "}"
        if hasattr(item, "name"):
            return item.name
        return str(item)
    
    def eval_expr(self, expr):
        stack = list()
        traceback = []
        try:
            for (i, token) in enumerate(expr):
                traceback.append(str(stack))
                token = token.lower().strip()
                if token.isnumeric():
                    stack.append(int(token))
                    continue
                if token.startswith('"') and token.endswith('"'):
                    stack.append(token[1:-1])
                    continue
                if hasattr(self, "func_" + token):
                    func = getattr(self, "func_" + token)
                    args = list()
                    if len(stack) < func.__code__.co_argcount - 1:
                        raise Exception("Insufficient parameters for '{token}'".format(token=token))
                    for i in range(func.__code__.co_argcount - 1):
                        args.append(stack.pop())
                    stack += func(*args)
                    continue
                raise Exception("Unknown token '{token}'".format(token=token))
        except Exception as e:
            e.traceback = traceback
            raise e
        return stack
    
    @commands.command(pass_context=True)
    async def nf(self, ctx, *, expr):
        try:
            result = self.eval_expr(expr.split())
        except Exception as e:
            print("notforth exception: " + str(e))
            print('\n'.join(e.traceback))
            print("\n")
            await ctx.send(":robot: An error has occured```\n" + str(e) + "```See console for traceback")
            return
        await ctx.send("```" + self.custom_print(result) + "<-- top```")

def setup(bot):
    bot.add_cog(NotForth(bot))