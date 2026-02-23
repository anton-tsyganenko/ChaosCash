Personal bookkeeping application, inspired by GnuCash.

The project is in early development — do not use in production. Backward compatibility may be broken at any time.

### What makes ChaosCash different:

* **Extreme multicurrency support**: While other multicurrency applications allow you to create accounts in different currencies, ChaosCash completely removes the link between an account and a single currency. Any account can track multiple currencies simultaneously.

* **Smart split recalculation**: In transactions more complex than a simple one-debit/one-credit entry, ChaosCash can automatically recalculate amounts to prevent imbalance and reduce unnecessary manual work. This is especially useful when duplicating complex transactions to create a similar one with a different total amount.

* **Technical simplicity**: ChaosCash gives you full structural freedom — no fixed chart of accounts, no enforced accounting rules. You can debit or credit any account in any currency (or any unit defined in your currencies table). You are even free to create imbalances — ChaosCash will warn you, but it will not restrict you.

* **Precise transaction timestamps**: Each transaction stores exact timing, making it easy to sort and distinguish multiple transactions created on the same day.

* **Flexible decimal separators**: Both comma and dot are accepted as decimal separators when entering numbers, unless you use one of them as a thousands separator. This small but recurring frustration has been eliminated.
