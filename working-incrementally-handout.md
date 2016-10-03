# Day 1 morning: Working incrementally

> 1/2 day: "working incrementally".  Writing tests and getting them to pass is
> all very well, but it's still easy to get into trouble.  Have you ever set
> off to make some changes to your code, and found yourself several hours into
> the effort, with changes to half a dozen files, everything is broken, many
> tests failing, and starting to worry about how you're ever going to get
> things working again?  This course is aimed at teaching the technique of
> working incrementally -- how to make changes to a codebase in small steps,
> going from "working state to working state", based on a series of practical
> examples.

## Prep (which naturally everyone has already done, naturally)

```
mkvirtualenv tdd-workshop --python=python3
pip install 'django<1.9' selenium
git clone https://github.com/hjwp/book-example.git tdd-workshop
cd tdd-workshop
git checkout chapter_06
python manage.py test # should all pass.
```


## Intro

Check out the code:

    git checkout incremental-workshop-start
    git checkout -b working-incrementally


Harry to give a quick tour of the site, outline what works now,
what we want to achieve.


## First exercise: hack it together as quickly as poss!

Get multiple lists for multiple people working!  Each should have its own URL

* Try to get the FT to pass
* And, ideally, with a set of passing unit tests too (but worry about them
  later if you like)


## Discussion: on working incrementally

* How many people got it working?
* Was it hard?  What steps did you go through?
* Obv this is a simple example.


## Quick overview: what we want to achieve.  Breaking it down.

Now let's do it the incremental way.

  - BDUF vs lean discussion
  - start todo list
  - model layer
  - brief REST discussion


## Harry demo session 1, on working incrementally

Here's our to-do list:

* Adjust model so that items are associated with different lists
* Add unique URLs for each list
* Add a URL for creating a new list via POST
* Add URLs for adding a new item to an existing list via POST

What can we pick off as a small, achievable task that will move
us towards our solution without breaking anything, getting back
to a working state asap?


-> Harry live-code demo.


## Break

Fika!


## Second exercise:  another small chunk.

What next?

* Adjust model so that items are associated with different lists
* *Add unique URLs for each list* (started)
* Add a URL for creating a new list via POST
* Add URLs for adding a new item to an existing list via POST


  git stash # or commit, or new branch, or whatever you like
  git reset --hard incremental-workshop-step-2

This tag includes a couple of failing unit tests for you to get passing.

  * create new url, for view that doesnt exist yet
  * create dummy view
  * make the unit tests pass one by one, redirect first, then saving data
  * point the form at the new URL
  * re-run the FT and confirm things still work
  * red/green/refactor:
    - remove redundant unit tests for `home_page`
    - strip out redundant code from `home_page`

If in doubt, follow along with the book, here:
[http://www.obeythetestinggoat.com/book/chapter_06.html#_another_url_and_view_for_adding_list_items](chapter 6) 


## Discussion of first two small steps (11:25)

* How did y'all get on?
* Any reactions?


## Final exercise:  try and finish!

Option 1: follow the book

- models change first
- unbreak all unit tests
- regression / partial credit: now have many lists of maximum one item.
- create new view+url for adding to existing list

Option 2: Harry's alternative (untested) plan

- create new url for adding to existing list first, based on only-list-in-world
- use {% url %} entries
- switch from hardcoded -only-list to a param in add_item and view_list
- models change, 
- but use get_or_create in homepage to create the only list in world, and
  redirect.
- now switch to multiple lists

Option 3: choose your own adventure!

* always try to get back to a working state as quickly as you can

* and do lots of commits!


## Wrap-up

If I haven't mentioned them, ask about:

* refactoring cat
* the kata analogy
* the bucket of water and the well


