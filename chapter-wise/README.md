# Chapter Wise

Suite `ATurjEWGS499niuWP` — 6 cases accumulated against
`shop.qaautomationlabs.com`, the running example for end-to-end checkout.

The full flow (`86c7da12…`) logs in with `demo@demo.com` / `demo`, shops from the
Men Fashion category, and completes a nine-field checkout:

```
click "Shop Now" below the "Men Fashion"
click "Add to Cart" below the "Black T-Shirt"
scroll up
click "1"                      <- the cart link matches only its item-count badge
click "Proceed To Checkout"
... First Name, Last Name, E-mail, Mobile No., Address, State, City, Pin Code
click "Continue"
click "Place Order"
check that page contains "Thank You for Your Order!"
```

Two details this suite teaches, both visible in the steps:

- **The cart is reached by `click "1"`.** The icon carries no caption of its own;
  the item-count badge is its only text.
- **Checkout is two stages.** `Continue` moves to review, `Place Order` commits.
  A test that stops after `Continue` has not placed an order.

The remaining cases are earlier drafts of the same journey — one stops after the
first checkout field, one uses placeholder text as field descriptors
(`enter "kailash@qa.com" into "example@email.com"`), and
`5138dcad…` is a one-line UI-objects sketch.
