
# Sprint Retrospective

## Start

I will start writing characterization tests before modifying legacy code. My baseline and test commits preserve the original implementation and record its observable behaviour. The tests cover both connection types, slab boundaries, senior discounts, previous dues, invalid types, printed output and receipt strings.

I will also start making small changes that can be tested and reviewed independently. My Git history contains [actual number] refactoring commits.

## Stop

I will stop assuming that existing calculations follow the business rules I expect. The senior discount is applied after tax is calculated, and it only applies to household bills. Changing this order would alter existing results.

I will stop combining multiple refactorings into one large commit. During this assignment, [describe an actual failed test or state that all tests passed without a failure].

## Continue

I will continue running `python3 -m pytest -q` after every refactoring step. The tests saved me when [describe a real example from your work]. I will retain descriptive names, named constants and shared calculation functions.

## Action items

1. I will run pytest before every refactoring commit, starting with the next module.
2. I will review the Git diff after every extraction, before committing.
