# todo_list.py
# add, delete, show

import discord
from discord.ext import commands
import re
import os

from discord.utils import to_json


class Todo:
    # init
    def __init__(self, date, label, item):
        #  see if the date is valid
        d = re.compile("[0-9]{1,2}/[0-9]{1,2}")
        assert d.match(date)
        self.date = date
        self.label = label
        self.item = item

    
    def __lt__(self, other):
        return self.date< other.date
        
    def __eq__(self, other):
        return self.date==other.date and self.label==other.label and self.item==other.item

   
    def __repr__(self):
        return f"{self.date} {self.label} {self.item}"
# open file in read mode
lines= []
def open_file():
    with open('record_the_todo_list', 'r') as file_handle:
        global lines
        lines = file_handle.read().splitlines()
        c= 0
        for line in lines:
            z= line.split(' ', 2)
            data= z[0]
            label= z[1]
            item= z[2]
            line= Todo(data, label, item)
            lines[c]= line
            c+= 1
open_file()

class Todo_list(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
        # open file in read mode
        self.todo_list =lines
    # read file content into list
    # $add date label item
    @commands.command(
        help = '''
        Add TODO.
        For example:
        $add 06/24 Sprout Discord Bot HW
        ''', 
        brief = "Add TODO." 
    )
    async def add(self, ctx, date, label, *, item):
        try:
            
            t = Todo(date, label, item)
            print(self.todo_list)
        except Exception as e:
            
            print(e)
            await ctx.send("Invalid input ><") 
            return
        
        self.todo_list.append(t)
         
        self.todo_list.sort()
        with open('record_the_todo_list', 'w') as f:
            for line in self.todo_list:
                f.write(str(line))
                f.write('\n')
        open_file()
      
        await ctx.send('"{}" added to TODO list'.format(item))
    # $done date label item
    @commands.command(
        help = '''
        Done TODO.
        For example:
        $done 6/24 Sprout Discord Bot HW
        ''', 
        brief = "Done TODO."
    )
    async def done(self, ctx, date, label, *, item):
        try:
            t = Todo(date, label, item)
            if t in self.todo_list:
                self.todo_list.remove(t)
            with open('record_the_todo_list', 'w') as f:
                for line in self.todo_list:
                    f.write(str(line))
                    f.write('\n')
            open_file()
        except Exception as e:
            
            print(e)
            await ctx.send("Invalid input ><")
            return
        
        await ctx.send('"{}"  delete from TODO list'.format(item))
       

    # $show [label]
    @commands.command(
        help = '''
        Show all TODO with the label if specified sorted by date.
        For example:
        $show Sprout
        $show
        ''',
        brief = "Show all TODO with the label if specified sorted by date." 
    )
    async def show(self, ctx, label=None):
        try:
            t = label
            if label== None:
                label=  "all" 
                for i in self.todo_list:
                    await ctx.send(i)
            else:
                self.todo_list.sort()
                for l in self.todo_list:
                    if l.label== t:
                        await ctx.send(l)
        except Exception as e:
            
            print(e)
            await ctx.send("Invalid input ><")
            return
        
        await ctx.send('show {} todo_list '.format(label))
       
 
    # $clear
    @commands.command(help = "Clear TODO list.", brief = "Clear TODO list.")
    async def clear(self, ctx):
        self.todo_list.clear()
        open('record_the_todo_list', 'w').close()
        
        await ctx.send('successfully clear all the information in the todo_list!!!')
def setup(bot):
    bot.add_cog(Todo_list(bot))
