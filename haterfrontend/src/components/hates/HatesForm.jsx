import React from "react";
import { useState, useRef } from "react";
import "./Hates.css";
import { useSelector } from "react-redux";

export default function HatesForm({ toggle, setToggle }) {
  const hateInput = useRef(null);
  const user = useSelector((state) => state.user);

  const handleSubmit = async (event) => {
    event.preventDefault();
    let postOptions = {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("knox")}`,
      },
      body: JSON.stringify({
        h_body: hateInput.current.value,
        haters: user.id,
      }),
    };
    fetch(`https://haterbackend.herokuapp.com/createHate`, postOptions)
      .then((res) => res.json())
      .then((data) => {
        if (!data["error"]) {
          setToggle((prev) => !prev);
          hateInput.current.value = "";
        } else {
          alert(data["error"]);
        }
      });
  };

  return (
    <div className="hate-text-box">
      <div className="hate-profile-textbox">
        <div className="hate-profile-pic">
          <img
            src={`https://avatars.dicebear.com/api/adventurer/${user.name}.svg?flip=1`}
            alt="profile"
          ></img>
        </div>
      </div>
      <div className="hates-form">
        <form className="hates-form-box" onSubmit={handleSubmit}>
          <input
            ref={hateInput}
            className="hates-form-text"
            placeholder="Who's Hatin'"
            name="h_body"
            maxLength="140"
            type="text"
            required
          />
          <div className="hates-form-button-container">
            <input className="hates-button-up" type="submit" value="Hate" />
          </div>
        </form>
      </div>
    </div>
  );
}
