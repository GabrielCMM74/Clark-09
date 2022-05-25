# `SEI` Week 10 Quiz - Answer Key

## For this quiz, please slack your instructors the answers, in numbered order. Do not include the questions. For example:
    1. Swag
    2. Yolo

## React JSX and Props

1. What JSX would render a `Person` component, and provide to it a `name` prop with a value of "Fred"?

    #### Solution: 

    ```js
    <Person name="Fred" />
    ```

2. Given the following component: 

    ```jsx
    export default function App() {
      const person = {
        first: "Sammy",
        last: "Hagar",
        company: "ACME Corp"
      };
      return (
        <Person person={...} />
      );
    }
    ```

    What would you replace the `...` with in order to pass the entire `person` object?
 
    #### Solution:

    ``` js
    person
    ```

3. Assuming the above `<App>` component and the following `<Person>` component:

    ```jsx
    export default function Person() {
      return (
        <article>
          <h5>{props.first} {props.last}</h5>
          <p>Company: {props.company}</p>
        </article>
      );
    }
    ```

    Re-write the single line of code so that the `<Person>` component renders as intended?

    #### Solution:

    ```jsx
    export default function Person(props) {
    ```

4. Assuming the following `<Info>` component:

    ```jsx
    export default function Info() {
      const title = 'Tesla';
      const engineType = 'Electric';
      const isFast = true;
      return (
        <article>
          <p>{title}</p>
          <p>Type: {engineType}</p>
          <p>Fast: {isFast}</p>
        </article>
      );
    }
    ```

    What will be displayed in the browser by rendering the `<Info>` component?

    #### Solution:

    ```
    Tesla
    Type: Electric
    Fast:
    ```


## React State and Hooks

5. Given the following code, what will the data type of the `resultOfCallingUseState` be?

    ```js 
    const resultOfCallingUseState = useState(null);
    ```

    #### Solution:

    ```
    array (of course, arrays are objects in JS)
    ```

6. Given the following code within a component:

    ```js
    const [todo, setTodo] = useState(null);
    ```

    What is `setTodo` used for?

    #### Solution:

    ```
    setTodo is a "setter" function used to update/replace the value held in the todo state variable.
    ```

7. Given the following component:

    ```jsx
    export default function Person() {
      const [name, setName] = useState('Jenny');

      function changeName() {
        setName('Jorge');
        console.log(name);
      }

      return (
        <article>
          <h5>{name}</h5>
        </article>
      );
    }
    ```

    What would be logged in the console if the `changeName` function was invoked for the first time?

    #### Solution:

    ```
    Jenny
    (setter functions are asynchronous therefore name will not be updated until the next render)
    ```

 7. In general, why were hooks added to React?

``` 
solution: It allowed function components to perform behavior that was previously limited to class components
```

## React Event Handling

8. What change in the code will make the following code work as intended when the `<button>` is clicked?


    ```jsx
    export default function Person() {
      const [name, setName] = useState('Jenny');

      return (
        <article>
          <h5>{name}</h5>
          <button onClick={setName('Jorge')}>Change name to Jorge</button>
        </article>
      );
    }
    ```

    #### Solution

    ```jsx
    onClick={() => setName('Jorge')}
    ```

## Miscellaneous

9. What is the best array iterator method for converting an array of data into an array of components to be rendered?

    #### Solution:

    ```
    map
    ```

10. What is the best array **iterator method** for removing an object from an array?

    #### Solution:

    ```
    filter
    ```
