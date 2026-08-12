# Forms and `v-model`

**Lab-backed example:** [`pages/forms.vue`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab/blob/main/pages/forms.vue) · [Open the live page](https://resux-lab.vercel.app/forms)

The Resux Lab form exercises text inputs, a select, a checkbox, submit prevention, a reset button and conditional output. Each field is backed by `useState()` so the page also checks compiler handling of `v-model` with resumable state.

## Form state

```vue
<script setup lang="ts">
const name = useState('form-name', () => '')
const email = useState('form-email', () => '')
const plan = useState('form-plan', () => 'starter')
const agreed = useState('form-agreed', () => false)
const saved = useState('form-saved', () => false)

function saveForm() {
  saved.value = true
}
</script>
```

## Bind native form controls

```vue
<form @submit.prevent="saveForm">
  <input placeholder="Name" v-model="name" />
  <input placeholder="Email" v-model="email" />

  <select v-model="plan">
    <option value="starter">Starter</option>
    <option value="scale">Scale</option>
    <option value="enterprise">Enterprise</option>
  </select>

  <label>
    <input type="checkbox" v-model="agreed" />
    I agree to test Resux form resume behavior.
  </label>

  <button type="submit">Save state</button>
</form>
```

The lab renders a live preview beside the form so each control can be checked independently before submit.

## Reset several fields in one action

```ts
function clearForm() {
  name.value = ''
  email.value = ''
  plan.value = 'starter'
  agreed.value = false
  saved.value = false
}
```

This is a useful regression pattern because one handler updates several bindings with different value types.

## Conditional confirmation

```vue
<p v-if="saved">Saved in resumable state.</p>
```

Use server-side validation for trust and security. Client state and `v-model` improve interaction, but they do not replace validation at the API/server boundary.

## Related

- [Template Syntax](/guide/template-syntax)
- [State and Reactivity](/guide/state)
- [Server API](/guide/server-api)
- [Input component](/components/input)
- [Select component](/components/select)
