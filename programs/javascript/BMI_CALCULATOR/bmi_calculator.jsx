import React, { useState } from "react";

const Bmi_Calculator = () => {
  const [user_weight, set_user_weight] = useState("");
  const [user_height, set_user_height] = useState("");
  const [bmi_value, set_bmi_value] = useState(null);
  const [bmi_message, set_bmi_message] = useState("");

  const calculate_bmi = (e) => {
    e.preventDefault();

    if (user_weight === "" || user_height === "") {
      set_bmi_message("Please enter valid values");
      set_bmi_value(null);
      return;
    }

    const height_in_meters = user_height / 100;
    const calculated_bmi = (user_weight / (height_in_meters * height_in_meters)).toFixed(1);
    set_bmi_value(calculated_bmi);

    if (calculated_bmi < 18.5) set_bmi_message("Underweight 😟");
    else if (calculated_bmi < 24.9) set_bmi_message("Normal weight 😊");
    else if (calculated_bmi < 29.9) set_bmi_message("Overweight 😐");
    else set_bmi_message("Obese 😟");
  };

  const reset_form = () => {
    set_user_weight("");
    set_user_height("");
    set_bmi_value(null);
    set_bmi_message("");
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500">
      <div className="bg-white/20 backdrop-blur-lg shadow-2xl rounded-2xl p-8 w-[90%] max-w-md text-center border border-white/30">
        <h1 className="text-3xl font-bold text-white mb-6 tracking-wide">
          BMI Calculator
        </h1>
        <form onSubmit={calculate_bmi} className="flex flex-col gap-4">
          <input
            type="number"
            placeholder="Enter your weight (kg)"
            value={user_weight}
            onChange={(e) => set_user_weight(e.target.value)}
            className="p-3 rounded-xl border-none outline-none text-center text-lg bg-white/80"
          />
          <input
            type="number"
            placeholder="Enter your height (cm)"
            value={user_height}
            onChange={(e) => set_user_height(e.target.value)}
            className="p-3 rounded-xl border-none outline-none text-center text-lg bg-white/80"
          />
          <button
            type="submit"
            className="bg-gradient-to-r from-green-400 to-blue-500 text-white font-semibold py-3 rounded-xl hover:scale-105 transition-all duration-300"
          >
            Calculate BMI
          </button>
          <button
            type="button"
            onClick={reset_form}
            className="bg-white text-gray-800 font-semibold py-3 rounded-xl hover:bg-gray-100 transition-all duration-200"
          >
            Reset
          </button>
        </form>

        {bmi_value && (
          <div className="mt-6 bg-white/30 rounded-xl p-4 shadow-md">
            <h2 className="text-2xl font-bold text-white">
              Your BMI: <span className="text-yellow-200">{bmi_value}</span>
            </h2>
            <p className="text-lg text-white mt-2">{bmi_message}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Bmi_Calculator;
