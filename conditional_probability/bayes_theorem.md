# Bayes' Theorem

Bayes' theorem is a way to figure out conditional probability. **Conditional probability** is the probability of an event happening, given that it has some relationship to one or more other events. For example, your probability of getting a parking space is connected to the time of day you park, where you park, and what conventions are going on at any time (conditional factors to be considered as part of your model). Bayes' theorem is slightly more nuanced. In a nutshell, it gives you the actual probability of an **event** given information about **tests**.

- `Events` are different from `tests`. For example, there is a test for a disease, but that's separate from the event of actually having the disease.
- Tests are flawed: just because you have a positive test does not mean you actually have the disease. Many tests have a high `false positive` rate. **Rare events tend to have higher false positive rates** than more common events. Bayes' theorem takes the test results and calculates your *real probability* that the test has identified the event.

```
P(A|B) = P(B|A)P(A)/P(B)
```

`P(A|B)` is the `posterior` - the probability of model parameter `A` being true, given the data `B`.

`P(B|A)` is the `likelihood` - given model parameter `A` what is the likelihood of obtaining the data `B`.

`P(A)` is the `prior` - the probability of the model parameter `A` being true.

`P(D)` is the `evidence` - the probability of getting the data, given all possible model parameter values.

## Example 1
You might be interested in finding out a patient's probability of having liver disease if they are an alcoholic. "Being and alcoholic" is the `test` for liver disease.

- `A` could mean the event "patient has liver disease". Past data tells you that `10%` of patients entering your clinic have liver disease - `P(A)=0.10`.
- `B` could mean the litmus test that "patient is an alcoholic". `5%` of the clinic's patients are alcoholics - `P(B)=0.05`.
- You might also know that among those patients diagnosed with liver disease `7%` are alcoholics. This is your `P(B|A)` - the probability that a patient is alcoholic, given that they have liver disease is `7%`.

```
P(A|B) = (0.07 * 0.1)/0.05 = 0.14
```

In other words, if the patient is an alcoholic, their chances of having liver disease is `14%`. This is a large increase from the `10%` suggested by past data. But it's still unlikely that any particular patient has liver disease.