---
name: redux
description: Provides comprehensive guidance for Redux state management including
  stores, actions, reducers, middleware, selectors, and Redux Toolkit. Use when the
  user asks about Redux, needs to manage global state, implement Redux patterns, or
  work with Redux middleware.
license: Apache-2.0
metadata:
  hermes:
    category: react-ecosystem
    provider: react
    repo: full-stack-skills/react-skills
---

# Redux

Provides comprehensive guidance for Redux state management including stores, actions, reducers, middleware, selectors, and Redux Toolkit. Use when the user asks about Redux, needs to manage global state, implement Redux patterns, or work with Redux middleware.

## When to use this skill

Use this skill whenever the user wants to:
- 用 Redux 管理 React 应用全局状态（store、reducer、action、dispatch）
- 使用 Redux Toolkit（createSlice、configureStore）或经典写法

## How to use this skill

1. **核心**：store、reducer、action、dispatch； useSelector、useDispatch。
2. **Toolkit**：createSlice、configureStore、createAsyncThunk；DevTools 与中间件。
3. **参考**：https://react-redux.js.org/ 、https://redux-toolkit.js.org/

## Best Practices

- 状态扁平、按域切 reducer；action 与 reducer 纯函数。
- 异步用 thunk 或 RTK Query；避免在 reducer 中请求。

## Keywords

redux, Redux Toolkit, store, 状态管理, React

## Procedure

1. Verify prerequisites and runtime environment.
2. Execute relevant operations or CLI actions for redux.
3. Review generated logs or outputs.

## Pitfalls

- Avoid executing unverified configurations or missing required credentials.
- Ensure schema boundaries and timeouts are respected.

## Verification

- Inspect exit status and command outputs.
- Run verification check to confirm redux functions as expected.
