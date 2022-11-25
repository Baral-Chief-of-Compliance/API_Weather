<template>
    <input type="text" @input="$emit('input', $event.target.value)">
</template>

<script>
export default {
    model: {
        prop: 'value',
        event: 'input'
    }
}
</script>
<style>

</style>