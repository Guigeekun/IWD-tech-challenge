# Notes

## Workflow
We have two branchs

- Master
- Develop

I'll work on develop and "release" sometimes to master when some big stuff get done.

## Why is there no issues ?
Usually we have quite a precise workflow when working on projects.

Make an issue, create a branch, merge it.

This workflow got many benefits, 
- traceability
- maintainability
- readability

...

This project is a bit different from a regular one, first of all i'm working alone on it and more importantly, it is not meant to be maintained.

This is why i'll skip the workflow to save some time.

## Why are you passing url and headers as args ?
To make some reusable components, I try to handle these kind of *config vars* as if I was doing `dependency injection`.

By giving those as arg we might be able to reuse the function for many other usages, maybe even in other projects.
