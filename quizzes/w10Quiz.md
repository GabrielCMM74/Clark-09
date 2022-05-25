# `SEI` Week 10 Quiz

## For this quiz, please slack your instructors the answers, in numbered order. Do not include the questions. For example:
    1. Swag
    2. Yolo

## React JSX and Props

1. What JSX would render a `<Person>` component, and provide to it a `name` prop with a value of "Fred"?

2. Given the following component: 

    ```jsx
    import Person from './Person';

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


## React State and Hooks

5. Given the following code, what will the data type of the `resultOfCallingUseState` be?

    ```js 
    const resultOfCallingUseState = useState(null);
    ```
 
6. Given the following code within a component:

    ```js
    const [todo, setTodo] = useState(null);
    ```

    What is `setTodo` used for?
 
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

## Miscellaneous

9. What is the best array iterator method for converting an array of data into an array of components to be rendered?

10. What is the best array **iterator method** for removing an object from an array?

