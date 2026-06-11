
function ResultCard({ result }) {

    const baseURL = "http://127.0.0.1:8000";


    const riskColor = {

        "No Tumor":
            "bg-green-600",

        "Low Risk":
            "bg-green-500",

        "Moderate Risk":
            "bg-yellow-500 text-black",

        "High Risk":
            "bg-red-600"

    };


    return (

        <div className="mt-10 max-w-6xl mx-auto">

            <h2 className="
            text-4xl 
            font-bold 
            text-center 
            mb-8
            text-cyan-400">

                AI Analysis Report

            </h2>


            {/* Stats Section */}

            <div className="
            grid 
            md:grid-cols-4 
            gap-4">


                <div className="card p-5 rounded-2xl text-center">

                    <h3 className="text-gray-400">
                        Tumor Status
                    </h3>

                    <p className="text-xl font-bold mt-2">

                        {
                        result.tumor_detected
                        ?
                        "Detected"
                        :
                        "Not Detected"
                        }

                    </p>

                </div>


                <div className="card p-5 rounded-2xl text-center">

                    <h3 className="text-gray-400">
                        Affected Region
                    </h3>

                    <p className="text-xl font-bold mt-2">

                        {result.tumor_percentage} %

                    </p>

                </div>



                <div className="card p-5 rounded-2xl text-center">

                    <h3 className="text-gray-400">
                        Confidence
                    </h3>

                    <p className="text-xl font-bold mt-2">

                        {result.confidence} %

                    </p>

                </div>



                <div className="card p-5 rounded-2xl text-center">

                    <h3 className="text-gray-400">
                        Risk Level
                    </h3>


                    <span className={`
                    px-4 
                    py-2 
                    rounded-full 
                    font-bold
                    mt-2
                    inline-block
                    ${riskColor[result.report.risk_level]}
                    `}>

                        {result.report.risk_level}

                    </span>

                </div>


            </div>



            {/* Medical Report */}

            <div className="
            card 
            rounded-3xl 
            p-6 
            mt-8">


                <h3 className="
                text-2xl 
                font-bold 
                mb-4">

                    AI Medical Summary

                </h3>


                <p className="mb-3">

                    <b>Scan ID:</b>
                    {result.report.scan_id}

                </p>


                <p className="mb-3">

                    <b>Date:</b>
                    {result.report.date}

                </p>


                <p className="mb-3">

                    <b>Finding:</b>
                    {result.report.finding}

                </p>


                <p className="text-gray-300">

                    {result.report.summary}

                </p>


                <hr className="my-4 opacity-30"/>


                <p className="text-sm text-red-300">

                    ⚠️ {result.report.disclaimer}

                </p>


            </div>



            {/* Images Section */}


            <div className="
            grid 
            md:grid-cols-3 
            gap-6 
            mt-8">


                <ImageCard
                    title="Original MRI"
                    src={
                        baseURL + result.images.mri
                    }
                />


                <ImageCard
                    title="Tumor Mask"
                    src={
                        baseURL + result.images.mask
                    }
                />


                <ImageCard
                    title="AI Overlay"
                    src={
                        baseURL + result.images.overlay
                    }
                />


            </div>


        </div>

    );
}



function ImageCard({ title, src }) {


    return (

        <div className="
        card 
        rounded-3xl 
        p-4">


            <h3 className="
            text-center 
            font-bold 
            mb-4">

                {title}

            </h3>


            <img
                src={src}
                alt={title}
                className="
                rounded-xl 
                w-full 
                shadow-lg
                hover:scale-105
                duration-300"
            />


        </div>

    );

}


export default ResultCard;