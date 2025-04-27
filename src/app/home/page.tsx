import React from "react";

export default function Page() {
  return (
    <>
      <div className="bg-sky-300 w-[50%] h-screen flex items-center justify-center">
        <div className="rounded-[2vw] drop-shadow-lg bg-white text-center w-[70%] h-[40%]"> 
          <p className="text-[2.5rem]">Click an icon to find nearby services.</p>
          <img className="w-[10rem]" src="/public/clip-art-for-dinner-13.png"></img>
          <div className="flex gap-8 items-center justify-center pt-[3rem] text-[2rem]">
            <div className="rounded-[1vw] h-[15rem] w-[13rem] bg-gray-100">
            hi
            </div>
            <div className="rounded-[1vw] h-[15rem] w-[13rem] bg-gray-100">
              
            hi
            </div>
            <div className="rounded-[1vw] h-[15rem] w-[13rem] bg-gray-100">
            hi
            </div>
          </div>
        </div>
      </div>
    </>
  )

}