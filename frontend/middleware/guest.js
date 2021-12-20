export default function ({ context,store, redirect }) {
    if (store.state.loggedIn) {
      return redirect('/')
    }
  }