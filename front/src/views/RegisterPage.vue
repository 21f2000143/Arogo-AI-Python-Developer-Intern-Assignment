<template>
  <FormCompo>
    <template v-slot:form>
      <h5 class="card-title">Register Patient</h5>
      <form @submit.prevent="submitForm">
        <div class="mb-3">
          <label class="form-label">Username</label>
          <input type="text" v-model="username" class="form-control" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Email address</label>
          <input type="email" v-model="email" class="form-control" required>
          <div v-if="message" class="alert alert-warning">
            {{ message }}
          </div>
        </div>
        <div class="mb-3">
          <label class="form-label">Name</label>
          <input type="text" v-model="name" class="form-control" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Age</label>
          <input type="number" v-model="age" class="form-control">
        </div>
        <div class="mb-3">
          <label class="form-label">Gender</label>
          <select class="form-select" v-model="gender" required>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
        <div class="mb-3">
          <label class="form-label">Contact</label>
          <input type="text" v-model="contact" class="form-control" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Medical History</label>
          <textarea class="form-control" v-model="medical_history" type="text" id="medical_history" name="medical_history" required></textarea>
        </div>
        <div class="mb-3">
          <label class="form-label">Password</label>
          <input type="password" v-model="password" class="form-control" required>
        </div>
        <button type="submit" class="btn btn-outline-primary">Register</button>
      </form>
    </template>
  </FormCompo>
</template>

<script>

import FormCompo from '../components/FormCompo.vue';
import home from '../utils/navigation.js';
export default {
  name: 'RegisterPatientPage',
  components: {
    FormCompo
  },
  data() {
    return {
      username: '',
      email: '',
      name: '',
      age: null,
      gender: null,
      contact: '',
      medical_history: '',
      password: '',
      message: ''
    }
  },
  methods: {
    home() {
      home(this.$store, this.$route, this.$router);
    },
    async submitForm() {
      try {
        const response = await fetch('http://127.0.0.1:8000/register-patient/', {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            "username": this.username,
            "email": this.email,
            "name": this.name,
            "age": this.age,
            "gender": this.gender,
            "contact": this.contact,
            "medical_history": this.medical_history,
            "password": this.password
          }),
        });
        if (response.ok) {
          const data = await response.json();
          alert("Patient registered successfully");
          if (this.$route.path != '/login') {
            this.$router.push('/login')
            this.home()
          }
        } else {
          const data = await response.json();
          throw new Error(data.error);
        }
      } catch (error) {
        alert(error);
      }
    },
  }
}
</script>
