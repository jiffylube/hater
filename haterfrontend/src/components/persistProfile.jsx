import React, { useEffect } from "react";
import { store } from "../state/store";

export default function PersistProfile() {
  useEffect(() => {
    let knoxToken = localStorage.getItem("knox");
    if (knoxToken) {
      let headerInfo = {
        Accept: "application/json",
        "Content-Type": "application/json",
        Authorization: `Token ${knoxToken}`,
      };
      let options = {
        method: "GET",
        headers: headerInfo,
      };
      fetch(`http://127.0.0.1:8000/user/grabProfile`, options)
        .then((res) => res.json())
        .then((data) => {
          store.dispatch({ type: "set", payload: data.profile });
        })
        .catch((err) => console.log(err));
    }
  }, []);

  return <></>;
}
