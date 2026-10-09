# expected

The transform of `before/views.py` into `after/views.py` must satisfy all of this; CI checks it.

## gone

- api.magic-status
- errors.bare-except

## remain

- errors.bool-in-except

`charge` returns a boolean to its callers; raising `NotEnoughMoney` instead would change public
behavior, so the finding stays and the explanation says what the callers would need.

## public

- charge(order, amount)
- create_order(request)
- order_detail(request, pk)
- NotEnoughMoney
