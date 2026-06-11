import { useState } from "react";

import Header from "./components/Header";
import UploadCard from "./components/UploadCard";
import Loading from "./components/Loading";
import ResultCard from "./components/ResultCard";


function App() {

    const [result, setResult] = useState(null);

    const [loading, setLoading] = useState(false);


    return (

        <div className="
        min-h-screen
        px-6
        py-10">


            {/* Logo & Title */}

            <Header />


            {/* Upload Section */}

            <UploadCard

                setResult={setResult}

                setLoading={setLoading}

            />


            {/* AI Processing Animation */}

            {

                loading && (

                    <div className="mt-8">

                        <Loading />

                    </div>

                )

            }


            {/* Results Dashboard */}

            {

                result && (

                    <ResultCard

                        result={result}

                    />

                )

            }


            {/* Footer */}

            <footer className="
            text-center
            text-gray-400
            mt-16
            pb-6">

                <p>
                    NeuroLens AI 
                </p>

                <p className="text-sm mt-1">

                    AI-assisted Brain MRI
                    Segmentation & Analysis

                </p>


                <p className="
                text-xs
                mt-4
                text-red-300">

                    This system provides
                    AI assistance only and
                    is not a substitute for
                    professional medical diagnosis.

                </p>

            </footer>


        </div>

    );
}


export default App;