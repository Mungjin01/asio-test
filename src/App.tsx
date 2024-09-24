import React from "react";

const App: React.FC = () => {
  const startAsio = () => {
    window.electron.startAsio();
  };

  return (
    <div>
      <h1>ASIO 드라이버 테스트</h1>
      <button onClick={startAsio}>시작</button>
    </div>
  );
};

export default App;
